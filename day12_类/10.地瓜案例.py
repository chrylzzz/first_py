class Spotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.conds = []

    def __str__(self):
        return f'这个地瓜烤了:{self.cook_time},状态:{self.cook_state},调料{self.conds}'

    def cook(self, time):
        """烤地瓜时间"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟的'
        elif self.cook_time >= 8:
            self.cook_state = '糊了'

    def add_conds(self, cond):
        self.conds.append(cond)


spotato = Spotato()
spotato.cook(5)
spotato.cook(1)
spotato.cook(3)
spotato.add_conds('🍅')
spotato.add_conds('🍆')
print(spotato)
