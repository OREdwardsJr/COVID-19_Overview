# COVID-19 Overview

An overview of COVID-19 cases in the USA through the usage of SQLite.

<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />


  <h3 align="center">:mask:COVID-19 Overview:mask:</h3>

  <p align="center">
    An analysis of 1000 reported cases of COVID in the United States. This project isn't intended to provide a meaningful extrapolation of the provided data. However, it provides you with all of the tools needed to connect to the CDC's API and insert it into SQLite, or your preferred SQL language.
    <br />
    <a href="https://github.com/oredwardsjr/COVID-19_Overview"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/oredwardsjr/COVID-19_Overview">View Demo</a>
    ·
    <a href="https://github.com/oredwardsjr/COVID-19_Overview/issues">Report Bug</a>
    ·
    <a href="https://github.com/oredwardsjr/COVID-19_Overview/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This Python project connects to Socrata Open Data API (SODA) to obtain this free dataset from the CDC. The API retrieves 1000 rows. However, there are 6 million rows of data accessible via download as XML or CSV. While I chose to use the 1000 rows, this program will work for the larger dataset as well. If you decide to download the full dataset please ensure that you have the adequate RAM and disk space. It's recommended that you use the smaller dataset if you are not comfortable handling large data.


<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python](https://docs.python.org/3/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [Requests](https://docs.python-requests.org/en/latest/user/quickstart/)
- [SQLite](https://docs.python.org/3/library/sqlite3.html)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Fork the project to your local machine. While SQLite comes with Python, Pandas and Requests do not and you will need both to run this package. It is a best practice to create a virtual environment prior to installing external libraries. If you are unaware of how to do so then here the [official documentation](https://docs.python.org/3/library/venv.html) on doing so. 


<!-- USAGE EXAMPLES -->
## Usage

This project is setup to connect to most public APIs and convert them into an SQL database. You will need to clean the data to your liking.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Obtain number of cases per state
- [ ] Add state populations to database
- [ ] Calculate deaths per state

See the [open issues](https://github.com/othneildrew/COVID-19_Overview/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Orlando Edwards Jr - [LinkedIn](https://linkedin.com/in/orlando-edwards-jr)

Project Link: [https://github.com/OREdwardsJr/COVID-19_Overview](https://github.com/OREdwardsJr/COVID-19_Overview)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [CDC Covid Open Source](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [JSON of States and Their Abbreviations](https://gist.github.com/mshafrir/2646763#file-states_hash-json)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/COVID-19_Overview.svg?style=for-the-badge
[covid-url]: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4
[forks-shield]: https://img.shields.io/github/forks/othneildrew/COVID-19_Overview.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/COVID-19_Overview/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/COVID-19_Overview.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/COVID-19_Overview/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/COVID-19_Overview.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/COVID-19_Overview/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/COVID-19_Overview.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/COVID-19_Overview/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/orlando-edwards-jr/
[product-screenshot]: images/screenshot.png
