#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.


def get_torchbiggraph_config():

    config = dict(  # noqa
        # I/O data
        entity_path="data/dbpedia-2015-04/bg_edit",
        edge_paths=[
            "data/dbpedia-2015-04/bg_edit/train_partitioned",
            "data/dbpedia-2015-04/bg_edit/valid_partitioned",
            "data/dbpedia-2015-04/bg_edit/test_partitioned",
        ],
        checkpoint_path="model/dbp1504",
        # Graph structure
        entities={"all": {"num_partitions": 1}},
        relations=[
            {
                "name": "all_edges",
                "lhs": "all",
                "rhs": "all",
                "operator": "complex_diagonal",
            }
        ],
        dynamic_relations=True,
        # Scoring model
        dimension=100,
        global_emb=False,
        comparator="dot",
        # Training
        num_epochs=5,
        num_uniform_negs=1000,
        loss_fn="softmax",
        lr=0.1,
        #regularization_coef=1e-3,
        # Evaluation during training
        eval_fraction=0,  # to reproduce results, we need to use all training data
    )

    return config
