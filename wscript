## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('applications', ['internet', 'config-store','stats'])
    module.source = [
        'model/bulk-send-application.cc',
        'model/new-send-application.cc',
        'model/onoff-application.cc',
        'model/packet-sink.cc',
        'model/new-packet-sink.cc',
        'model/ping6.cc',
        'model/radvd.cc',
        'model/radvd-interface.cc',
        'model/radvd-prefix.cc',
        'model/udp-client.cc',
        'model/udp-server.cc',
        'model/seq-ts-header.cc',
        'model/udp-trace-client.cc',
        'model/packet-loss-counter.cc',
        'model/udp-echo-client.cc',
        'model/udp-echo-server.cc',
        'model/v4ping.cc',
        'model/application-packet-probe.cc',
        'helper/bulk-send-helper.cc',
        'helper/on-off-helper.cc',
        'helper/packet-sink-helper.cc',
        'helper/ping6-helper.cc',
        'helper/udp-client-server-helper.cc',
        'helper/udp-echo-helper.cc',
        'helper/new-packet-sink-helper.cc',
        'helper/new-send-helper.cc',
        'helper/v4ping-helper.cc',
        'helper/radvd-helper.cc',
        ]

    applications_test = bld.create_ns3_module_test_library('applications')
    applications_test.source = [
        'test/udp-client-server-test.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'applications'
    headers.source = [
        'model/bulk-send-application.h',
        'model/new-send-application.h',
        'model/onoff-application.h',
        'model/packet-sink.h',
        'model/new-packet-sink.h',
        'model/ping6.h',
        'model/radvd.h',
        'model/radvd-interface.h',
        'model/radvd-prefix.h',
        'model/udp-client.h',
        'model/udp-server.h',
        'model/seq-ts-header.h',
        'model/udp-trace-client.h',
        'model/packet-loss-counter.h',
        'model/udp-echo-client.h',
        'model/udp-echo-server.h',
        'model/v4ping.h',
        'model/application-packet-probe.h',
        'helper/bulk-send-helper.h',
        'helper/on-off-helper.h',
        'helper/packet-sink-helper.h',
        'helper/ping6-helper.h',
        'helper/udp-client-server-helper.h',
        'helper/udp-echo-helper.h',
        'helper/new-packet-sink-helper.h',
        'helper/new-send-helper.h',
        'helper/v4ping-helper.h',
        'helper/radvd-helper.h',
        ]

    bld.ns3_python_bindings()
