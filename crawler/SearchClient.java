import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class SearchClient {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("🔍 Enter search query:");
        String query = scanner.nextLine();

        try {
            // 1. Create the 'Phone' (HttpClient)
            HttpClient client = HttpClient.newHttpClient();

            // 2. Prepare the 'Call' (Request) 
            // We replace spaces with %20 so the URL doesn't break
            String url = "http://127.0.0.1:8000/search?query=" + query.replace(" ", "%20");
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .build();

            // 3. Make the call and catch the response
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // 4. Show the result
            System.out.println("\n--- RESPONSE FROM PYTHON ---");
            System.out.println(response.body());
            System.out.println("----------------------------");

        } catch (Exception e) {
            System.out.println("❌ Error: Could not talk to Python. Is app.py running?");
            e.printStackTrace();
        }
    }
}
