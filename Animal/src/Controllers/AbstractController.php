<?php

namespace Bank\Controllers;

use Bank\Core\Request;
use Bank\Utils\DependencyInjector;

abstract class AbstractController {
    protected $request;
    protected $db;
    protected $config;
    protected $view;
    protected $log;
    protected $customerId;
    protected $di;

    public function __construct(DependencyInjector $di, Request $request) {
        $this->request = $request;
        $this->di = $di;
        $this->db = $di->get("PDO");
        $this->log = $di->get("Logger");
        $this->view = $di->get("Twig_Environment");
        $this->config = $di->get('Utils\Config');
    }

    public function setCustomerId(int $customerId) {
        $this->customerId = $customerId;
    }

    protected function render(string $template, array $params): string {
        return $this->view->loadTemplate($template)->render($params);
    }
}