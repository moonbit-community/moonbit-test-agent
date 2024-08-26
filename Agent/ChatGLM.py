from langchain_community.chat_models import ChatZhipuAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
zhipuai_api_key = '4a478b99108ee30c1ae4aaa0aefe6632.X8sj7A6gaBgWh9AE'
llm = ChatZhipuAI(
    api_key=zhipuai_api_key,
    model="glm-4-9b:772570335:v1:mjbhkmfk",
    temperature=0.5,
)

loader = TextLoader(file_path="./MoonBit.md", encoding="utf-8")
docs = loader.load()
prompt = ChatPromptTemplate.from_template("""作为一名MoonBit语言工程师，你的任务是编写一系列测试用例来验证项目中的正确性。请根据以下提供的格式，完成对给出的MoonBit代码的测试：
测试格式参考：
test {{
    assert_eq(fib2(1))
    assert_eq(fib2(2))
    assert_eq(fib2(3))
    assert_eq(fib2(4))
    assert_eq(fib2(5))
}}
MoonBit代码片段：{question}。
    """)

retriever_chain = (
    {"question":RunnablePassthrough() }
    | prompt
    | llm
    | StrOutputParser()
)

re = retriever_chain.invoke("""
fn num_water_bottles(num_bottles: Int, num_exchange: Int) -> Int {
  fn consume(num_bottles, num_drunk) {
    if num_bottles >= num_exchange {
      let num_bottles = num_bottles - num_exchange + 1
      let num_drunk = num_drunk + num_exchange
      consume(num_bottles, num_drunk)
    } else {
      num_bottles + num_drunk
    }
  }
  consume(num_bottles, 0)
}
""")
print(re)