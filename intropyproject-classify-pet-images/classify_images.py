#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Natasha E. Estrada
# DATE CREATED:   4/11/2023                              
# REVISED DATE:  4/12/2023
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 

from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
       # Runs classifier function to classify the images 
       model_label = classifier(images_dir+key, model)

       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase and strip whitespace
       model_label = model_label.lower().strip()
       truth = results_dic[key][0]
       truth = truth.lower().strip()
              
       # Adds classifier label and the value of 1 (match) or 0 (not a match) 
       # to the results_dic dictionary for the key indicated by the variable key 
       if truth in model_label:
           results_dic[key].extend([model_label, 1])
       else:
           results_dic[key].extend([model_label, 0])
