from Database_Code.ingest_data import load_swebench, transform_dataset, debug_print_example, connection, run_schema


def main(): 
    debug_print_example()
    conn = connection()
    run_schema(conn)



if __name__ == "__main__":
    main()