import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Scanner;

public class Menu {

    public void menu() {
        Scanner scanner = new Scanner(System.in);
        int opcao = 0;
        int idCounter = 0;
        String descricao, url, data;
        Site site;
        File directory = new File("sites");
        directory.mkdir();

        while (opcao != 4) {
            System.out.println("1 - Cadastrar site");
            System.out.println("2 - Listar sites");
            System.out.println("3 - Buscar site");
            System.out.println("4 - Sair");
            System.out.print("Digite a opção desejada: ");
            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {
                case 1:
                    idCounter++;
                    System.out.print("Digite a descrição do site: ");
                    descricao = scanner.nextLine();
                    System.out.print("Digite a url do site: ");
                    url = scanner.nextLine();
                    System.out.print("Digite a data de cadastro do site: ");
                    data = scanner.nextLine();
                    site = new Site(idCounter, descricao, url, data);
                    salvarSite(site);
                    break;
                case 2:
                    listarSites();
                    break;
                case 3:
                    System.out.print("Digite o id do site: ");
                    int id = scanner.nextInt();
                    scanner.nextLine();
                    buscarSite(id);
                    break;
                case 4:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
        }
        scanner.close();
        
    }

    private static void salvarSite(Site site) {
        try (ObjectOutputStream objectOutputStream = new ObjectOutputStream(
                new FileOutputStream("sites/" + site.getId() + ".data"))) {
            objectOutputStream.writeObject(site);
            System.out.println("Site salvo com sucesso!");
        } catch (IOException e) {
            System.out.println("Erro ao salvar o site: " + e.getMessage());
        }
    }

    private static void listarSites() {
        File directory = new File("sites");
        File[] siteFiles = directory.listFiles();
        if (siteFiles != null) {
            for (File siteFile : siteFiles) {
                try (ObjectInputStream objectInputStream = new ObjectInputStream(
                        new FileInputStream(siteFile))) {
                    Site site = (Site) objectInputStream.readObject();
                    System.out.println(site);
                } catch (IOException | ClassNotFoundException e) {
                    System.out.println("Erro ao listar os sites: " + e.getMessage());
                }
            }
        } else {
            System.out.println("Nenhum site cadastrado.");
        }
    }

    private static void buscarSite(int id) {
        File file = new File("sites/" + id + ".data");
        if (file.exists()) {
            try (ObjectInputStream objectInputStream = new ObjectInputStream(
                    new FileInputStream(file))) {
                Site site = (Site) objectInputStream.readObject();
                System.out.println(site);
            } catch (IOException | ClassNotFoundException e) {
                System.out.println("Erro ao buscar o site: " + e.getMessage());
            }
        } else {
            System.out.println("Site não encontrado.");
        }
    }
}
