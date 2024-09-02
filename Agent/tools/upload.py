from zhipuai import ZhipuAI

client = ZhipuAI(api_key="4a478b99108ee30c1ae4aaa0aefe6632.X8sj7A6gaBgWh9AE")

resp = client.knowledge.document.create(
    file=open("../dataset.jsonl", "rb"),
    purpose="fine-tune",
    knowledge_id="1002",
)
print(resp)
