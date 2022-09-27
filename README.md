## Inspiration
Law and justice are concepts that safeguard democracy and the pillars of a successful society. After witnessing the protests this past year and the general trend regarding the ruling of laws in the country, we decided to see if it was possible for us to make a small difference in the world.

The name of our app, Themis, comes from the Ancient Greek goddess Themis who is said to be the manifestation of justice, order, fairness, and law. Reading about her and seeing her symbolism in the modern age, the statue referred to as "Lady Justice", inspired us to create an app that follows from her ideal and the statue.

An app that was blind to the noise around it, weighed the scales equally and gave just and fair reasoning for their decisions. Not only did we want the concept of fairness and equality to be reflected in the services offered but also in our own methodology in building the app.

## What it does
We extract text from Supreme Court decisions that have been publicly made available.

After extraction, we extract five useful pieces of information: a summary of the decision, what judges were present and what they voted, the category of the decision, and the historical context as to why the case was brought forward to the public.

We then input the data into our database and pass that onto the website which displays the data in easy-to-understand information cards and interactive graphs for trend analysis.

Our UI ensures that users can freely explore, read, and learn more about these pivotal cases that inform the past, present, and future of our society.

## How we built it
We access Supreme Court opinions published on the website of the Supreme Court of the USA and use a web crawler to get access to the browser and access the pdf links they have put out. The pdf links link to the decision and other information is encoded on the website regarding the decision. We use a web scraper to scrape the general information and then extract the text from the PDFs.

After extraction, we use the SpaCy model to be able to do extractive summarization - this refers to using the sentences in the text to create a summary. With this tool, we are able to create a summary for the decision and the historical context.

In addition, we utilize NLTK tokenization to be able to pick up the Supreme Court justices that are present in the paper - only using the paper itself! In addition, we are able to find distinctions within their voting such as unanimous, majority, concurring, and dissenting opinions within these justices.

We also work with the Washington University Law School and their impressive Supreme Court Database which accesses decisions from 1947 up to 2020 and labels them which issue area they correspond to in society. We are able to join these two datasets and add the categories as per the indication in the database.

Once the model has run on all the PDFs, we store all the data regarding into a MongoDB structure which then works with our React frontend to beautifully display a landing page, the decisions page, and the graphical analysis page.

In addition, we developed a RESTful API that allows us to implement filters in our decisions and graphical analysis page.

Finally, the entire website is hosted and run, in production, on Heroku.

## Challenges we ran into
One of the main challenges we ran into was the continual merging of the backend and front end. From previous experiences, we know that these two components in a working environment are very different and are prone to cause problems when connected. We had a lot of problems in the beginning when even assembling and connecting the modeling to the database backend. Later on, that evolved into merging the front and backend. We had a lot of discussions regarding merge conflicts and what's the best way to move forward to save time.

Another big challenge was deployment - initially, we tried to deploy with AWS, Heroku (ironic), and Flask, however, all those options failed us. For a while, we just gave up on deploying however through consistent searching, debugging, and reading Heroku documentation, we were able to connect our project and have our API on the website.

## Accomplishments that we're proud of
We are incredibly proud of each other as some of us were working with certain technologies for the first time and others were dealing with complex issues that would riddle our brains!

As a team, we are proud of our website and its aesthetic style. We believe it strikes the perfect balance between professional but also sleek and modern. In addition, our ability to get the votes for justice to be extracted and our summarized texts are a big point of pride for us.

## What we learned
We learned about the complexities of deploying and maintaining it in production. We also had the biggest learning curve with React and learning how to use and understand concepts like reactive elements, working with templates, and many more. The challenges faced in coding with React allowed us to innovate and be more creative with our UI and as such, we ended up learning the most in that department.

## What's next for Themis
The next big step is improving the summarization model. While researching, we came up with another model - Flair - which has shown to be more effective than SpaCy at summarizing law cases. In addition, applying more advanced NLP scraping and cleaning techniques is a must as the pdf is a giant mixture of unknown symbols, weird punctuation, and a syntax that is unlike the English we speak. Improving those two aspects will allow us to become even stronger in the services we offer.

## Built With
beautiful-soup
fastapi
github
heroku
javascript
mongodb
nltk
nosql
orm
python
react
spacy
