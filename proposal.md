# Project Proposal

## Motivation and Purpose
Our role: Data scientists/Dog enthusiasts!

Target audience: Prospective dog owners and those who work in the dog business

Picking out your new furry friend can be difficult, especially when you do not know what kind you want! With our DoggoDash, we aim to assist those in making a decision as to what kind of dog fits their preferences best and give insight to what kind of breeds are the highest rated in certain fields. Our visualization and recommendation tools will make this process simple by allowing the user to filter for specific dog traits and even use our selection algorithm to see which dog fits them the best.

## Description of the Data
We will be visualizing the [Dog breeds](https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-02-01) dataset from the American Kennel Club (AKC). The dataset consists of three .csv files:

  1. **breed_traits**: This files provides trait information on each dog breed (`Breed`) by assigning scores on a scale of 1-5 for each trait (`Trait_Score`). Some trait examples are Affectionate With Family, Coat Type, Adaptability Level, and more.  
  2. **breed_rank_all**: This files contains the popularity ranking of each dog breed by AKC registration statistics from 2013-2020 (`2013 Rank` - `2020 Rank`). We can also get the links to the image and the AKC webpage of each dog breed from this file.
  3. **trait_description**: This file gives detailed descriptions of each trait and its corresponding scores. Hence, this file acts more like a dictionary for the columns and values in the `breed_traits` file. 

Using this data, we plan to visualize a list of top five favorite dog breeds based on the user’s preferences of dog traits. 

## Research Questions and Usage Scenarios
