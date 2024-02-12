(python -m pip list --format freeze) -match '==' -replace '==','>=' > delrequirement.txt
python -m pip install --upgrade --requirement delrequirement.txt

## https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/
# python -m pip install --upgrade pip
# pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
