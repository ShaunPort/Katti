TYPE=('didntLike','smallDoses','largeDoses')

class Couple(object):
    """约会对象

    Attributes:
        distance 情侣飞行距离
        gameRate 情侣游戏时间 率
        iceRate 情侣冰淇淋 率
        type: Type 约会类型
    """

    distance=0
    gameRate=0
    iceRate=0
    type=TYPE[0]

    def __init__(self) -> None:
        """初始化"""
        pass
    
    def __init__(self,ls=[]) -> None:
        """初始化
        
        约会对象类初始化

        Args:
            ls->[]
            ls[0] distance: float 飞行距离
            ls[1] gameRate: float 情侣游戏时间 率
            ls[2] iceRate: float 情侣冰淇淋 率
            ls[3] type: Type 约会类型
        Raises:
            TypeError     
        """
        self.distance=ls[0]
        self.gameRate=ls[1]
        self.iceRate=ls[2]
        self.type=ls[3]


    def __str__(self) -> str:
        """toString
        Returns:
            String
        """
        return 'distance:'+str(self.distance)+',gameRate:'+str(self.gameRate)+',iceRate:'+str(self.iceRate)+'\ntype:'+self.type








if __name__=='__main__':
    a=Couple([1000,2,3,TYPE[1]])
    print(a)
