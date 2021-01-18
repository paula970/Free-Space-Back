from fastapi import FastAPI
import os
import sys
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{parametros}")
async def root(parametros):
    #os.system("py malloc.py -S 100 -b 1000 -H 4 -a 4 -l ADDRSORT -p BEST -n 5 -c")
    output = os.popen("py malloc.py " + parametros).read().replace('\n',"")
    return output
    