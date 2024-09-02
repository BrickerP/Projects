Instructions
Run data_generate.py. This will create two sample files: flow_logs.txt, lookup_table.csv
Run get_results.py to process the flow logs and produce output_results.csv.

Data Format
The flow logs follow the format outlined in the AWS VPC Flow Logs documentation.

Assumptions
The lookup table is provided via email.
Protocol values are mapped as follows: 6 = TCP 17 = UDP
All files (flow_logs.txt, lookup_table.csv, and output_results.csv) are generated and processed within the same directory as the Python scripts.