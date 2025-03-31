/**
 * Function to mask clouds using the Sentinel-2 QA band
 * @param {ee.Image} image Sentinel-2 image
 * @return {ee.Image} cloud masked Sentinel-2 image
 */
function maskS2clouds(image) {
    var qa = image.select('QA60');
  
    // Bits 10 e 11 são nuvens e cirrus, respectivamente.
    var cloudBitMask = 1 << 10;
    var cirrusBitMask = 1 << 11;
  
    // Ambas as flags devem ser zero para indicar condições limpas.
    var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
        .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  
    return image.updateMask(mask).divide(10000);
  }
  
  var dataset = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                    .filterDate('2024-07-01', '2025-03-01')
                    .filterBounds(ee.Geometry.Point([-43.0928, -19.8306])) // Coordenadas de Bela Vista de Minas
                    .map(maskS2clouds);
  
  var visualization = {
    min: 0.0,
    max: 0.3,
    bands: ['B4', 'B3', 'B2'],
  };
  
  Map.setCenter(-43.0928, -19.8306, 12);
  
  print(dataset.features);

  // dataset.toList(dataset.size()).evaluate(function(images) {
  //   images.forEach(function(imageInfo) {
  //     var img = ee.Image(imageInfo.id);
  //     var timestamp = imageInfo.properties['system:time_start'];
  
  //     if (timestamp) {  // Verifica se o timestamp não é null
  //       var date = ee.Date(timestamp).format('YYYY-MM-dd').getInfo();
  //       Map.addLayer(img, visualization, 'Imagem ' + date);
  //     }
  //   });
  // });
  