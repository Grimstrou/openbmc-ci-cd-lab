# Dockerfile
FROM jenkins/jenkins:lts-jdk17

USER root

# Установка Python и зависимостей
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        git \
    && \
    rm -rf /var/lib/apt/lists/*

# Установка Python-пакетов
RUN pip3 install --break-system-packages unittest-xml-reporting

# Проверка установки (опционально, для отладки)
RUN python3 -c "import xmlrunner; print('✅ xmlrunner installed')"

USER jenkins