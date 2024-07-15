from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


def main():
    # Set up Spark configuration and context
    # conf = SparkConf().setAppName("WordCount").setMaster("Lorem")
    # sc = SparkContext(conf=conf)

    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    sc = spark.sparkContext

    # Read the input text file
    # input_file = "/opt/spark/spark-events/data/input.txt"
    input_file = "/opt/spark/data/input.txt"
    text_file = sc.textFile(input_file)

    # Perform the word count
    counts = (
        text_file.flatMap(lambda line: line.split(" "))
        .map(lambda word: (word, 1))
        .reduceByKey(lambda a, b: a + b)
    )

    # Save the result to an output directory
    output_dir = "/opt/spark/data/output"
    counts.saveAsTextFile(output_dir)

    # Stop the Spark context
    sc.stop()


if __name__ == "__main__":
    main()
