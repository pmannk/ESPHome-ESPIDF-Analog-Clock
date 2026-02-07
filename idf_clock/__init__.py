import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID

idf_clock_ns = cg.esphome_ns.namespace('idf_clock')
IDFClock = idf_clock_ns.class_('IDFClock', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(IDFClock),
    # Add your other custom config fields here
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
