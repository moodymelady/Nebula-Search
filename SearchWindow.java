import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class SearchWindow extends Application {
    private Label resultLabel = new Label("results will appear here");

    @Override
    public void start(Stage stage) {
        // configure search input field
        TextField searchBar = new TextField();
        searchBar.setPromptText("search nebula...");
        searchBar.setStyle("-fx-font-size: 16px; -fx-background-radius: 15; -fx-padding: 10;");

        // configure result display area
        resultLabel.setStyle("-fx-text-fill: white; -fx-font-size: 14px; -fx-padding: 10;");
        resultLabel.setWrapText(true);

        // handle enter key press
        searchBar.setOnAction(e -> {
            String query = searchBar.getText();
            resultLabel.setText("processing query...");
            
            // run network request in background thread
            new Thread(() -> {
                String response = askPython(query);
                javafx.application.Platform.runLater(() -> resultLabel.setText(response));
            }).start();
        });

        // layout container
        VBox root = new VBox(10, searchBar, resultLabel);
        root.setAlignment(Pos.CENTER);
        root.setStyle("-fx-background-color: #2b2b2b; -fx-background-radius: 15; -fx-padding: 20;");

        // stage configuration
        Scene scene = new Scene(root, 500, 250);
        scene.setFill(Color.TRANSPARENT);
        stage.initStyle(StageStyle.TRANSPARENT);
        stage.setScene(scene);
        stage.setAlwaysOnTop(true);
        stage.show();
    }

    private String askPython(String query) {
        try {
            // send http request to local python backend
            HttpClient client = HttpClient.newHttpClient();
            String encodedQuery = query.replace(" ", "%20");
            String url = "http://127.0.0.1:8000/search?query=" + encodedQuery;
            
            HttpRequest request = HttpRequest.newBuilder().uri(URI.create(url)).build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            return response.body();
        } catch (Exception e) {
            return "error: connection to python backend failed";
        }
    }

    public static void main(String[] args) { launch(args); }
}
