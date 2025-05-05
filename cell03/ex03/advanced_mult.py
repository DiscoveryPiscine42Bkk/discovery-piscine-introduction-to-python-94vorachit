#!/usr/bin/python3

table_num = 0
while table_num <= 10:
    i = 0
    print(f"Table de {table_num}:")
    while i <= 10:       
        print(f"{table_num * i}", end=" ")
        i += 1
    table_num += 1