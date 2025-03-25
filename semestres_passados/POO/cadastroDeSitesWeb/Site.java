import java.io.Serializable;

public class Site implements Serializable {

    private int id;
    private String descricao;
    private String url;
    private String data;

    public Site(String descricao, String url, String data) {
        this.descricao = descricao;
        this.url = url;
        this.data = data;
    }

    public Site(int id, String descricao, String url, String data) {
        this.id = id;
        this.descricao = descricao;
        this.url = url;
        this.data = data;
    }

    public int getId() {
        return id;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getUrl() {
        return url;
    }

    public String getData() {
        return data;
    }

    @Override
    public String toString() {
        return "Site{" +
                "id=" + id +
                ", descricao='" + descricao + '\'' +
                ", url='" + url + '\'' +
                ", data='" + data + '\'' +
                '}';
    }
}
