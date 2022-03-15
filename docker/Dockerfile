FROM conda/miniconda3



# open docker port
EXPOSE 8180/tcp

# define entry point
COPY docker/main.py src/main.py
ENTRYPOINT ["python", "src/main.py"]
# #}
