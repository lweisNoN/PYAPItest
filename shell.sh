# 打印当前文件路径
echo ${WORKSPACE}

echo "删除多余输出"
rm result.json
rm -rf Otput/*

echo "执行测试 python 脚本"
python FinalExam/Main.py

echo "转移数据"
mv result.json Output/result.json

echo "清理分支"
# git checkout .