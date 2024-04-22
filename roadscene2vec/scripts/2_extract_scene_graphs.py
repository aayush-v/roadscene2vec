import os
import sys
import json

sys.path.append(os.path.dirname(sys.path[0]))
import scene_graph.extraction.carla_extractor as CarlaEx
import scene_graph.extraction.image_extractor as RealEx
from util.config_parser import configuration
from util.script_exceptions import Invalid_Dataset_Type

#python 2_extract_scene_graphs.py --yaml_path ../config/scenegraph_extraction_config.yaml

'''This script runs scene graph extraction of Carla or Real data'''
def extract_scene_graphs(f):
    scene_config = configuration(sys.argv[1:])
    
    if scene_config.dataset_type == "carla":
        sg_extraction_object = CarlaEx.CarlaExtractor(scene_config)
        sg_extraction_object.load()
        scenegraph_dataset = sg_extraction_object.getDataSet() #returned scenegraphs from extraction
        scenegraph_dataset.save()
    elif scene_config.dataset_type == "image": #must calibrate birds eye view for real data
        sg_extraction_object = RealEx.RealExtractor(scene_config)
        graphVQA_sg = sg_extraction_object.load()
        json.dump(graphVQA_sg, f, indent=4)
        scenegraph_dataset = sg_extraction_object.getDataSet() #returned scenegraphs from extraction
        scenegraph_dataset.save()
    else:
        raise Invalid_Dataset_Type("Please input a valid dataset type")
        
    
if __name__ == "__main__":
    # scene_graph_path = '/data/courses/2024/class_cse59836295spring2024_rsenana1/group2/aayush/roadscene2vec/scenegraph_GraphVQA/Scene_graphs_indent.json'
    # f = open(scene_graph_path, 'w')
    f = ''
    extract_scene_graphs(f)