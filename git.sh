git add .
git commit -m "${1}"
git push origin master
echo -n "Pushed to origin master with commit message: "

echo ${1}
