import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Cria um veículo elétrico de exemplo
        ElectricVehicle electricVehicle = new ElectricVehicle("Model X", "Tesla", 600, 250, 80000);

        // Cria uma UF de exemplo
        List<String> topCities = new ArrayList<>();
        topCities.add("São Paulo");
        topCities.add("Rio de Janeiro");
        topCities.add("Belo Horizonte");

        State state = new State("São Paulo", "SP", "São Paulo", "23.5505° S, 46.6333° W", 44000000, 248209.426, topCities);

        // Pergunta ao usuário o formato desejado
        String selectedFormat = getUserSelectedFormat();

        // Converte e exibe a informação no formato selecionado
        switch (selectedFormat) {
            case "XML":
                String xmlOutput = convertToXML(electricVehicle, state);
                System.out.println("XML Output:");
                System.out.println(xmlOutput);
                break;
            case "JSON":
                String jsonOutput = convertToJSON(electricVehicle, state);
                System.out.println("JSON Output:");
                System.out.println(jsonOutput);
                break;
            case "YAML":
                String yamlOutput = convertToYAML(electricVehicle, state);
                System.out.println("YAML Output:");
                System.out.println(yamlOutput);
                break;
            default:
                System.out.println("Formato inválido. Escolha entre XML, JSON ou YAML.");
        }
    }

    private static String getUserSelectedFormat() {
        // Simule aqui a lógica para obter a escolha do usuário (por exemplo, via entrada do console).
        // Neste exemplo, estamos usando uma escolha fixa.
        return "JSON";
    }

    private static String convertToXML(ElectricVehicle electricVehicle, State state) {
        try {
            XmlMapper xmlMapper = new XmlMapper();
            String xml = xmlMapper.writeValueAsString(electricVehicle);
            xml += xmlMapper.writeValueAsString(state);
            return xml;
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    private static String convertToJSON(ElectricVehicle electricVehicle, State state) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String json = objectMapper.writeValueAsString(electricVehicle);
            json += objectMapper.writeValueAsString(state);
            return json;
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    private static String convertToYAML(ElectricVehicle electricVehicle, State state) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            String json = objectMapper.writeValueAsString(electricVehicle);
            json += objectMapper.writeValueAsString(state);

            // Converter o JSON para YAML
            DumperOptions options = new DumperOptions();
            options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
            Yaml yaml = new Yaml(options);

            Object data = yaml.load(json);
            return yaml.dump(data);
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }
}
