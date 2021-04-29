# Tables 
for i in range(2,20):
    with open(f"Tables/tables_fileWrite{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write("\n")