from datasets import load_dataset
import psycopg2
from pgvector.psycopg2 import register_vector
from psycopg2.extras import Json
from datetime import datetime
import json

# connects the postgresql database to this codebase 
def connection():
    conn = psycopg2.connect(
        dbname="swe_bench", # change to your database name if needed 
        user = "postgres", # change to your user if needed 
        password = "password", # change this to the password for postgres on your local machine 
        host = "localhost",
        port = 5432, # This is the port that your postgres is running on you local machine. change if needed 
        
    )
    with conn.cursor() as cur:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    conn.commit()
    register_vector(conn) #for pgvector extension 
    
    return conn

def run_schema(conn):
    with conn.cursor() as cur:
        schema_path = os.path.join(os.path.dirname(__file__), "Schema.sql")
        with open(schema_path, "r") as f: 
            sql = f.read()
            cur.execute(sql)
    conn.commit()




def load_swebench(split):
    # Load lite database 
    sbl = load_dataset('SWE-bench/SWE-bench_Lite', split=split)
    
    return sbl

#function to transform raw data in to a easily manipulated state 
def transform_dataset(sbl):

    for row in sbl:
        yield {
            "instance_id": row["instance_id"],
            "repo": row["repo"],
            "base_commit": row["base_commit"],
            "version": row["version"],
            "environment_setup_commit": row["environment_setup_commit"],

            "problem_statement": row["problem_statement"],
            "hint": row["hints_text"],  

            "patch": row["patch"],
            "test_patch": row["test_patch"],

            "created_at": row["created_at"],

            "fail_to_pass": row["FAIL_TO_PASS"],
            "pass_to_pass": row["PASS_TO_PASS"],

            "embedding": None,  
        }


# function to ensure that program is functioning as intended 
def debug_print_example(split="test", idx=0):
    sbl = load_swebench(split)
    mapped = next(transform_dataset(sbl))
    print(mapped)

