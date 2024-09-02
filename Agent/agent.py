from langchain_community.chat_models import ChatZhipuAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import argparse
import os
import glob

parser = argparse.ArgumentParser(description="用于加载API密钥和项目路径。")
parser.add_argument('--api_key', type=str, required=True, help='API密钥')
parser.add_argument('--path', type=str, default="./", help='测试目录的路径')
args = parser.parse_args()
zhipuai_api_key = args.api_key
path = args.path

llm = ChatZhipuAI(
    api_key=zhipuai_api_key,
    model="glm-4-9b:772570335:v1:mjbhkmfk",
    temperature=0.5,
)

prompt_template = ChatPromptTemplate.from_template("""作为一名MoonBit语言工程师，你的任务是编写一系列测试用例来验证项目中的正确性。请根据以下提供的格式，完成对给出的MoonBit代码的测试：  
测试格式参考：  
test {{  
    assert_eq(fib2(1))  
    assert_eq(fib2(2))  
    assert_eq(fib2(3))  
    assert_eq(fib2(4))  
    assert_eq(fib2(5))  
}}  
MoonBit代码片段：  
{questions}  
    """)


def process_mbq_files(directory_path):
    mbq_files = glob.glob(os.path.join(directory_path, "**", "*.mbt"), recursive=True)
    mbq_codes = []
    for file_path in mbq_files:
        with open(file_path, "r", encoding="utf-8") as file:
            mbq_code = file.read()
            mbq_codes.append(mbq_code)
    questions_str = "\n".join(mbq_codes)
    prompt_filled = prompt_template.format(questions=questions_str)
    response = llm.invoke(prompt_filled)
    parsed_response = StrOutputParser().parse(response.content)
    return parsed_response


parsed_response = process_mbq_files(path)

with open("test.mbt", "w", encoding="utf-8") as file:
    file.write(str(parsed_response) + "\n")