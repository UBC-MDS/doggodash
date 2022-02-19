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

### Research Questions

DoggoDash is designed to help potential dog owners find their favourite dog breeds by answering important questions they have before deciding to own one of them. Many dog breeds have certain consistent and standard attributes such as coat length, energy levels, young children friendly and many more. However, too many attributes can be confusing. 

Therefore, with the option to select few but most important attributes, DoggoDash with its interactive dashboard application can help answer the simplest yet most effective question - given certain attribute preferences, which are the best dogs to have.

### Usage scenario

Susane and David are a married couple, both in their thirties with two kids who are 2 years and 5 years old. They recently decided to add a pet dog to their family. They found several pet websites on the internet but with the overload of information, they are unable to decide on the best dog breed to have. Susane has a preference for energetic dogs while David has a preference for dogs with low coat length and low shedding frequency. When Susane and David log on to the "DoggoDash application", they will see a number of attributes to choose as filters. The maximum number of attributes they can choose as filters is 4. Once, they have choosen their preferred attributes as "filters", they will now tweak these filters based on a scale of 1 to 5 (low to high). Once done, the application displays  the top 5 dog breeds as per the choosen and tweaked attributes. With these  top five dog breeds, she now enquires about their prices, age, availability and other health related aspects of these breeds from the nearest pet shop and plans a visit to finalize one.
