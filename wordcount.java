import java.io.*;
import java.util.*;

public class wordcount {

    public static void main(String[] args) {

        // Check for input arguments
        if (args.length < 1) {
            System.out.println("Usage: java WordCountWithoutHadoop <input file>");
            System.exit(1);
        }

        String inputFile = args[0];
        Map<String, Integer> wordCountMap = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
            String line;

            // Read each line
            while ((line = br.readLine()) != null) {
                line = line.trim();

                // Split words by whitespace
                String[] words = line.split("\\s+");

                for (String word : words) {
                    if (!word.isEmpty()) {
                        // Convert to uppercase (like your Hadoop mapper)
                        word = word.trim().toUpperCase();

                        // Count occurrences
                        wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);
                    }
                }
            }

            // Print results (like reducer output)
            for (Map.Entry<String, Integer> entry : wordCountMap.entrySet()) {
                System.out.println(entry.getKey() + "\t" + entry.getValue());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


javac wordcount.java
java wordcount input.txt
