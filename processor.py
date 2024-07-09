import re
from fuzzywuzzy import fuzz
from utils import unescape_unicode
from titlecase import titlecase
import inflect

class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.p = inflect.engine()

    def process(self, data):
        processed_data = []
        for post in data['data']:
            bracketed_content = self.extract_bracketed_content(post['title'])
            if bracketed_content and not self.contains_excluded_words(post['title']):
                unescaped_content = unescape_unicode(bracketed_content)
                processed_title = self.post_process_title(unescaped_content)
                processed_data.append({"bracketed_title": processed_title, "created_utc": post['created_utc']})
        
        return self.combine_similar_titles(processed_data)

    def extract_bracketed_content(self, title):
        match = re.search(self.config.regex, title)
        return match.group(1) if match else None

    def contains_excluded_words(self, title):
        return any(word.lower() in title.lower() for word in self.config.exclude)

    def post_process_title(self, title):
        # Replace " S " with "'s "
        title = title.replace(' S ', "'s ")
        
        # Apply title case
        title = titlecase(title)
        
        # Clean and separate words
        title = re.sub(r'[^a-zA-Z\s]', ' ', title).strip()
        words = re.findall(r'\b[\w\'-]+\b', title)
        title = ' '.join(words)
        
        return title

    def combine_similar_titles(self, data):
        combined_data = {}
        for item in data:
            title = item['bracketed_title']
            matched = False
            for existing_title in combined_data:
                if self.is_similar(title, existing_title):
                    combined_data[existing_title]['count'] += 1
                    combined_data[existing_title]['timestamps'].append(item['created_utc'])
                    matched = True
                    break
            if not matched:
                combined_data[title] = {'count': 1, 'timestamps': [item['created_utc']]}
        return [{"bracketed_title": title, "count": data['count'], "timestamps": data['timestamps']} for title, data in combined_data.items()]

    def is_similar(self, title1, title2):
        # Check for exact match
        if title1.lower() == title2.lower():
            return True
        
        # Check for singular/plural match
        if self.p.singular_noun(title1.lower()) == title2.lower() or self.p.singular_noun(title2.lower()) == title1.lower():
            return True
        
        # Check fuzzy match
        if fuzz.ratio(title1.lower(), title2.lower()) > self.config.fuzzy_threshold:
            return True
        
        return False