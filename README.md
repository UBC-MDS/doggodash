# DoggoDash

Welcome to DoggoDash! DoggoDash is an interactive web app created using Dash and Python which provides visualizations for users to explore the breeds of dog that best match their selected preferences. Whether you are a potential new dog owner or are curious about your current dog breed's ranking among others, DoggoDash can help you!

Here is a preview of DoggoDash:

![DoggoDash Preview](docs/images/sketch.png)

## Installation

DoggoDash is hosted online by Heroku and can be accessed [here](http://dsci532-2022-group18-py.herokuapp.com/). There is no local installation required.

## Usage

Users can choose the dog traits of interest from the dropdown menu (i.e. Affectionate With Family, Coat Type, Adaptability Level, Trainability Level). Thereafter, the user can decide the importance of each selected trait according to their preference using the slider provided (i.e. Score 1 for the Affectionate With Family trait if the user prefers an independent dog). As a result of the preferences, our algorithm will return a list of top five dog breeds that fit your preferences the most (in descending order) and display it on the landing page of the app.

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/doggodash/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

DoggoDash is built using [Dash](https://dash.plotly.com/), and thus Dash is required for contributing to the project. Dash can be installed by running:
```
pip install dash
```
Once Dash is installed and the repository is cloned (following the instructions in the contributing guidelines), a local version of the app for testing can be built by running:
```
python src/app.py
```
Simply copy and paste the web address created into your browser of choice to begin seeing your changes come to life!

## License

`doggodash` was created by Samuel Quist, Steven Leung, Shiv Jena and Linh Giang Nguyen. It is licensed under the terms of the MIT license.

## Credits

`doggodash` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
