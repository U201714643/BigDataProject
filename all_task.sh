# counting status of tasks
python ./status_initializer.py | python  ./status_mapper.py | sort |python ./status_reducer.py

# jobduration 

python ./jobduration_