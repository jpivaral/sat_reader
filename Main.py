import xml.etree.ElementTree as ET
import click
import os

@click.command()
@click.option('--xml_path',
              required=True,
              help='Xml path')
def main(xml_path):
    files = os.listdir(xml_path)
    for file in files:
        if file.endswith('.xml'):
            print(f'FILE: {xml_path}/{file}')
            process_xml(f'{xml_path}/{file}')
            print('===========================================')

def process_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    version = '0.1.0'
    if '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation' in root.attrib and '0.2.0' in root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']:
        version = '0.2.0'
    descripcion = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}Descripcion'))
    nombres_impuestos = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}NombreCorto'))
    codigos_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}CodigoUnidadGravable'))
    cantidad_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}CantidadUnidadesGravables'))    
    montos_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}MontoGravable'))
    montos_impuestos = list(root.iter('{http://www.sat.gob.gt/dte/fel/'+version+'}MontoImpuesto'))
    
    for idx, val in enumerate(nombres_impuestos):
        print('impuesto: %s, gravable: %s, monto_gravable: %s, CantidadUnidadesGravables: %s, monto_impuesto: %s'%(
            val.text,
            codigos_gravables[idx].text if len(codigos_gravables) -1 >= idx else '',
            cantidad_gravables[idx].text if len(cantidad_gravables) -1 >= idx else '',
            montos_gravables[idx].text if len(montos_gravables) -1 >= idx else '',
            montos_impuestos[idx].text if len(montos_impuestos) -1 >= idx else ''
        ) )

if __name__ == "__main__":
    main()