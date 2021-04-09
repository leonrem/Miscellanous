###Leonid Rempel
###AIR Coding Assesment

### Creating a clean Slate ###
rm(list = ls()) # Clear environment
gc()            # Clear memory
cat("\f")       # Clear the console

### Checking for and loading our packages ###
packages <- c("ggplot2", # For graphs
              "ggthemes", # For thematic purposes
              "stargazer", # For charts/regression output
              "datasets")

for (i in 1:length(packages)) {
  if (!packages[i] %in% rownames(installed.packages())) {
    install.packages(packages[i]
                     , repos = "http://cran.rstudio.com/"
                     , dependencies = TRUE
    )
  }
  library(packages[i], character.only=TRUE)
}

### removing created variables to leave less of a footprint ###
rm(packages)
rm(i) 

### loading iris ###
data("iris")

### In the R script I use the simple summary command to answer a) ###
summary(iris)

### a) From the summary we see that there are 50 irises per specie.

### b) Scatterplot
ggplot(iris, aes(x = Petal.Length, y = Sepal.Length)) +
  
  #coloring according to species 
  geom_point(aes(color = factor(Species))) + 
  
  #my preferred theme
  theme_pander(base_family = 'mono') + 
  
  #labeling the graph
  labs(x = 'Petal Length', y = 'Speal Length',
       title = 'Sepal Length vs Petal Length', 
       color = 'Species') + 
  
  #this is just formatting the graph a little more
  theme(axis.title.x = element_text(size = 11, vjust=0, hjust = 0.5, family = 'mono'), 
        axis.title.y = element_text(size = 11, vjust=2, hjust = 0.5, family = 'mono'),
        plot.title = element_text(size = 13, hjust = 0.5, vjust = 1),
        plot.margin = unit(c(0.5, 1, 0.5, 1), "cm"),
        axis.line = element_line(linetype = 'solid', size = 0.4),
        plot.caption = element_text(size = 10, hjust = 0),
        axis.text.y = element_text(hjust = 0.5)) 

### Lets make our observations now! As we can see, 
### there seems to be an overall positive relationship 
### between petal length and sepal length. Furthermore, 
### the strength of this relationship varies by specie. 
### As for the sepal and petal lengths, the virginicia 
### has the largest measurements followed by the versicolor and the setosa.

### c) Multiple Regression
### Our next task is a multiple regression of petal length, 
### petal width and sepal width on sepal length. Lets see 
### if taking account of these extra variables changes 
### the relationship exhibited above in the scatterplot.

options(scipen = 3) # 3 decimal level percision
# our model
reg <- lm(Sepal.Length ~ Petal.Length + Petal.Width + Sepal.Width, iris) 

# this is the regression output
stargazer(reg, title="Multiple Regression Results", align = TRUE, header = FALSE) 

# Part d) Interpretation of Multiple Regression
### Looking at the above table, we see that, holding 
### petal width and sepal width constant, a 1 cm increase 
### in petal length is associated with, on average, a 0.709 cm 
### increase in sepal length. This effect is statistically 
### significant beyond the 1% level.

# Part e) EXTRA CREDIT
### I would like to see the effect by species. 
### As we saw in the scatter plot, the relationship 
### is different across species, so lets look at how different it is.

# our full model
reg2 <- lm(Sepal.Length ~ Petal.Length + Petal.Width + Sepal.Width + Species, iris) 

# this is the regression
stargazer(reg2, title="Multiple Regression Results with Species", align = TRUE, header=FALSE) 

### R chose the setosa as our base categorical variable. 
### Thus, all else equal, we see that Versicolors have, 
### on average, a Sepal length that is 0.724 cm smaller 
### than the Setosa and Virginicas have a sepal length 
### that is, on average, 1.023 cm smaller than the Setoa. 
### The effect of petal length on predicting speal length 
### is still significant and now predicts a 0.829 cm increase 
### in sepal length for each 1 cm increase in petal length, all else equal. 

### That concludes Q1. The other two questions are done in Python. 
