import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class SearchWindow extends Application {
    @Override
    public void start(Stage stage) {
        TextField searchBar = new TextField();
        searchBar.setPromptText("🔍 Search Nebula...");
        searchBar.setStyle("-fx-font-size: 20px;");

        StackPane root = new StackPane(searchBar);
        Scene scene = new Scene(root, 400, 100);

        stage.setTitle("Nebula Search");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
