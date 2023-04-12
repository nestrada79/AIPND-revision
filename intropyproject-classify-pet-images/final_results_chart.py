from prettytable import PrettyTable

# Create and populate the first table
num_images = PrettyTable()
num_images.field_names = ["# Total Images", "# Dog Images", "# Not-a-Dog Images"]
num_images.add_row([40, 30, 10])

# Print the first table
print(num_images)
print("\n\n\n")

# Create and populate the second table
results_table = PrettyTable()
results_table.field_names = ["CNN Model Architecture", "% Not-a-Dog Correct", "% Dogs Correct", "% Breeds Correct", "% Labels Matched", "Runtime (seconds)"]
results_table.add_row(["ResNet", "90%", "100%", "90%", "82.5%", 44])
results_table.add_row(["AlexNet", "100%", "100%", "80%", "75%", 15])
results_table.add_row(["VGG", "100%", "100%", "93.3%", "87.5%", 88])

# Print the second table
print(results_table)
    
print("VGG was able to classify 'dogs' and 'not-a-dog' with 100% accuracy and had\n"
      "the best performance regarding breed classification with 93.3% accuracy.\n"
      "AlexNet was the most efficient with the fastest runtime at only 3 seconds\n"
      "but still images 100% accuracy for identifying dogs correctly.")

  