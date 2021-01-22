FROM jupyter/tensorflow-notebook

RUN conda config --set auto_activate_base false

COPY requirements.txt .

RUN python3 -m venv /home/jovyan/test&& \
. /home/jovyan/test/bin/activate&& \
pip3 install -r requirements.txt&& \
python3 -m ipykernel install --user --name=test
