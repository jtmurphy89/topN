### Question 1:
What, for you, has been the most important technical innovation in 
Analytics in the last two years? Where are the shortcomings right now?

- I think the most important technical innovation in analytics 
in recent years has been the creation of open-source 
platforms, such as Airflow, to author, schedule and monitor analytics 
workflows. As data becomes more available, in higher volumes, at 
lower latency, greater stress is placed on the infrastructure, code and
processes that manage it. ETL failures are now so commonplace that lacking
clear visibility into when and why jobs fail puts quite a lot at stake. For
example, in my job at Eagle Point our analysts were frequently blocked 
because their data was missing, our engineers couldn't scale because they
were too busy correcting failures and our customers were angry 
that their dashboards were on the fritz. But using these organizational
tools alleviated a lot of these issues for us. By breaking up our 
ETL into more maintainable chunks with more accessible logging
and timely notification of failures, everyone can do their job faster and,
most importantly, our customers are much happier. 
- But no tool is absolutely perfect. A lot of these platforms require
pipelines to be authored using a programming language such as Python, 
which can be a barrier to entry for more SQL-savvy analysts, who might
require the help of an engineer. So I would say it's not as 
entirely self-serving as it could be for all working in the analytics 
space.


### Question 2:
Write a program, topN, that given an arbitrarily large file and a 
number, N, containing individual numbers on each line 
(e.g. 200Gb file), will output the largest N numbers, highest first. 
Tell me about the run time/space complexity of it, and whether you 
think there's room for improvement in your approach.
- I've written the function `topN` in the file `topN.py` along with some
tests in `topN_tests.py`
- Note that I'm assuming the file will contain only integers... 
Or, at least, that's the way i'm interpreting the
statement that the file contains "individual
numbers on each line."
- I claim that the run-time complexity of my topN function is O(Mlog(N)),
where M is number of lines in the file and N is the number of largest 
elements we are keeping track of.
- To see this: as we iterate over each of the M lines in the file, we are 
(worst case) performing a O(log(N)) pop and a O(log(N)) push onto
the min-heap, the run-time of which is, altogether, O(Mlog(N)). Finally, 
we perform a O(Nlog(N)) sort of the min-heap before returning. 
However, assuming M >> N, we should still have an overall runtime 
complexity of O(Mlog(N) + Nlog(N)) = O(Mlog(N))
- Space complexity: O(N) for the min-heap
- Room for improvement: there's always room for improvement!
- If we put the file into some kind of distributed storage (e.g. HDFS), 
allowing for the file to be broken up into smaller chunks with higher 
throughput, we could use a tool such as Spark to distribute the topN 
computation across many smaller partitions and then merge 
the results from each partition into a final topN list.
- Such an algorithm could look like the following:
    ```python 
    top_n = rdd \
        .mapPartitions(lambda itr: [topN(itr, n)] \
        .reduce(lambda x,y: topN(x + y, n))
    ```