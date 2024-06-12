# from typing import Dict, Union
# from pydantic import BaseModel  # 这是一个特别受欢迎的数据验证和设置库

# class MySchema(BaseModel):
#     name: str
#     age: int

# class BaseTool:
#     def __init_subclass__(cls, **kwargs) -> None:
#         super().__init_subclass__(**kwargs)
#         args_schema_type = cls.__annotations__
#         print(f"args_schema_type: {args_schema_type}")

# class MyTool(BaseTool):
#     args_schema: MySchema  # 为 args_schema 属性进行了类型注解
#     tool_name: str
#     tool_length: int
    
#     def __init__(self, args_schema, ):
        
        
    
    

# # 创建 MyTool 类实例时自动调用 __init_subclass__
# my_tool_instance = MyTool()



class Employee:
    params: str
    counter = 0

    def __init__(self, name: str, age: int, country: str):
        self.name = name
        self.age = age
        self.country = country
        type(self).counter += 1


print(Employee.counter)
jack = Employee('Jack', 20, 'cn')
print(Employee.counter)


back = Employee('Back', 20, 'cn')
print(Employee.counter)


cack = Employee('Cack', 20, 'cn')
print(Employee.counter)

print(Employee.__annotations__)
print(Employee.params)