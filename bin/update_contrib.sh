#!/bin/bash

git log --format='%aN <%aE>' | sort -u > CONTRIBUTORS
