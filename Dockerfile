FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install -U pandas numpy seaborn matplotlib scikit-learn scipy 

WORKDIR /home/doc-bd-a1/

COPY shopping_trends_updated.csv .

CMD ["bash"]