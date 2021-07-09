from os import CLD_EXITED
import xml.etree.ElementTree as ET
import click

@click.command()
@click.option('--xml_path',
              required=True,
              help='Xml path')
def main(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    nombres_impuestos = list(root.iter('{http://www.sat.gob.gt/dte/fel/0.1.0}NombreCorto'))
    codigos_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/0.1.0}CodigoUnidadGravable'))
    cantidad_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/0.1.0}CantidadUnidadesGravables'))    
    montos_gravables = list(root.iter('{http://www.sat.gob.gt/dte/fel/0.1.0}MontoGravable'))
    montos_impuestos = list(root.iter('{http://www.sat.gob.gt/dte/fel/0.1.0}MontoImpuesto'))
    
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