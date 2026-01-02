package cow_oop;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Word {
    String text;
    String meaning;
    char firstChar;
    char lastChar;
    Word next;
    
    Word(String text) {
        this.text = text;
        this.firstChar = text.charAt(0);
        this.lastChar = text.charAt(text.length() - 1);
        this.meaning = fetchMeaning(text);
        this.next = null;
    }
    
    private String fetchMeaning(String word) {
        try {
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://sozluk.gov.tr/gts?ara=" + word))
                .build();
            
            HttpResponse<String> response = client.send(request, 
                HttpResponse.BodyHandlers.ofString());
            
            String body = response.body();
            if(body.contains("[]")) {
                return "Kelime bulunamadı";
            }
            return "anlamı var.";
            
        } catch (Exception e) {
            return "anlamı yok.";
        }
    }
    
    public boolean isValid() {
        return !meaning.equals("böyle bir kelime yok.");
    }
}