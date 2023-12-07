class Job:
    def __init__(self, maJob, tenJob, tenNganh, tienLuong, **kwargs) -> None:
        self._maJob = maJob
        self._tenJob = tenJob
        self._tenNganh = tenNganh
        self._tienLuong = tienLuong
    
    def __str__(self) -> str:
        return f'Mã:{self._maJob} || Tên job: {self._tenJob} || Tên ngành: {self._tenNganh} || Tiền lương: {self._tienLuong}'
    
    def evaluate(self):
        average_score = self.evaluate_average()
        if 3.0 < average_score <= 5.0:
            # Lấy danh sách skill dưới 4.0
            low_skills = [skill_name for skill_name, skill_value in self.get_skills().items() if skill_value < 4.0]
            return f'Cần bổ sung thêm kiến thức\nDanh sách những skills < 4.0: {", ".join(low_skills)}' if low_skills else 'Tạm được'
        elif average_score > 9.0:
            return 'Rất phù hợp'
        elif average_score > 7.0:
            return 'Phù hợp'
        elif average_score > 5.0:
            return 'Tạm được'
        else:
            return 'Cần học lại kiến thức base'
        
    def get_skills(self):

        return {}

class AI(Job):
    def __init__(self, PythonSkill, MLSkill, DeepSkill, MathSkill, **kwargs):
        super().__init__(**kwargs)
        self.__PythonSkill = PythonSkill
        self.__MLSkill = MLSkill
        self.__DeepSkill = DeepSkill
        self.__MathSkill = MathSkill
        
    def evaluate_average(self):
        return (self.__PythonSkill + self.__MLSkill +  self.__DeepSkill +  self.__MathSkill) / 4

    def __str__(self) -> str:
        return super().__str__() + f' || Đánh giá: {self.evaluate()}'
    
    def get_skills(self):
        return {
            'Python Skill': self.__PythonSkill,
            'ML Skill': self.__MLSkill,
            'Deep Skill': self.__DeepSkill,
            'Math Skill': self.__MathSkill
        }

class Backend(Job):
    def __init__(self, SQLSkill, OOPSkill, ApiSkill, JavaSkill, **kwargs) -> None:
        super().__init__(**kwargs)
        self._SQLSkill = SQLSkill
        self._OOPSkill = OOPSkill
        self._ApiSkill = ApiSkill
        self._JavaSkill = JavaSkill
        
    def evaluate_average(self):
        return (self._SQLSkill + self._OOPSkill + self._ApiSkill + self._JavaSkill) / 4

    def __str__(self) -> str:
        return super().__str__() + f' || Đánh giá: {self.evaluate()}'
    
    def get_skills(self):
        return {
            'SQL Skill': self._SQLSkill,
            'OOP Skill': self._OOPSkill,
            'Api Skill': self._ApiSkill,
            'Java Skill': self._JavaSkill
        }

class Frontend(Job):
    def __init__(self, HtmlSkill, CssSkill, NodejsSkill, UX, UI, **kwargs) -> None:
        super().__init__(**kwargs)
        self._HtmlSkill = HtmlSkill
        self._CssSkill = CssSkill
        self._NodejsSkill = NodejsSkill
        self._UX = UX
        self._UI = UI
        
    def evaluate_average(self):
        return (self._HtmlSkill + self._CssSkill + self._NodejsSkill + self._UX + self._UI) / 5

    def __str__(self) -> str:
        return super().__str__() + f' || Đánh giá: {self.evaluate()}'
    
    def get_skills(self):
        return {
            'Html Skill': self._HtmlSkill,
            'Css Skill': self._CssSkill,
            'Nodejs Skill': self._NodejsSkill,
            'UX': self._UX,
            'UI': self._UI
        }
        
class Fullstack(Frontend, Backend):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def evaluate_average(self):
        return super().evaluate_average()
    
    def __str__(self) -> str:
        return super().__str__()
    
    def get_skills(self):
        return super().get_skills()

# Tạo đối tượng AI
ai_job = AI(PythonSkill=5, MLSkill=2, DeepSkill=5, MathSkill=1, maJob=1, tenJob='Data Scientist', tenNganh='AI', tienLuong=30000000)

# Tạo đối tượng Backend
backend_job = Backend(SQLSkill=2, OOPSkill=8, ApiSkill=7, JavaSkill=8, maJob=2, tenJob='Backend Developer', tenNganh='IT', tienLuong=25000000)

# Tạo đối tượng Frontend
frontend_job = Frontend(HtmlSkill=3, CssSkill=8, NodejsSkill=7, UX=8, UI=9, maJob=3, tenJob='Frontend Developer', tenNganh='IT', tienLuong=20000000)

# Tạo đối tượng Fullstack
fullstack_job = Fullstack(SQLSkill=2, OOPSkill=8, ApiSkill=7, JavaSkill=8, HtmlSkill=3, CssSkill=8, NodejsSkill=7, UX=8, UI=9, maJob=4, tenJob='Fullstack Developer', tenNganh='IT', tienLuong=30000000)

# In ra thông tin và đánh giá của các đối tượng
print(ai_job)
print(backend_job)
print(frontend_job)
print(fullstack_job)
