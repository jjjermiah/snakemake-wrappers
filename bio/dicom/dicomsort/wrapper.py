# FILEPATH: wrapper.py

# import the dicomsort module
import dicomsort


# Import the necessary modules
from snakemake.shell import shell

# Define the input, output, and parameters
input_files = snakemake.input.input_files
output_dir = snakemake.output.output_dir
params = snakemake.params

# Define the command to be executed
command = "dicomsort {input_files} {output_dir} {params}"

# Execute the command
shell(command)



