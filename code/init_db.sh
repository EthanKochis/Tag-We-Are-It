createdb project
psql project -f create_tables.sql
psql project -f create_view.sql
python3 insert_data.py
