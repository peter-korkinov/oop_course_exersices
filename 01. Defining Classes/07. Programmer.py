class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'

        return f'{self.name} does not know {language}'

    def change_language(self, new_lang, skills_needed):
        if self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'

        if new_lang == self.language:
            return f'{self.name} already knows {new_lang}'

        output = f'{self.name} switched from {self.language} to {new_lang}'
        self.language = new_lang
        return output
