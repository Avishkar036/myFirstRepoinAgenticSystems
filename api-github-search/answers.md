Q:"What is the role of quey parameters in this Question?"
Ans: In the following API request when we print the response without any paramters we get an lot of undesired data.To narrow down the reponse to desired feilds we have used different parameters. The paramneters used in the program are "q" which tells the name of query to be searched. Because of q parameter we can search specfic repositeries. The "sort" paramter helps to sort accoring to a criteria, in our case it is based on stars. The "order" parameter helps us set ascending or descending order of response.The "per_page" response limits the number of results in response by setting limit per page.

Q:"Why do we use response.json() instead of resonse.text()?"
Ans: ".text()" converts the response into a raw string, whereas ".json()" converts the response into python dictionary. Working and using an raw string in different operations is diffcult and hectic than an dictionary, that is why we use ".json()".
